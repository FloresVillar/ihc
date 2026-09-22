"""Provider adapters: one small class per LLM vendor, all exposing the same
`.chat(system_prompt, history) -> str` interface so the rest of the pipeline
(scenarios, judge, run_eval) never needs to know which vendor it's talking to.

Adding a new provider = write one class here implementing `.chat()` and
register it in PROVIDERS below. That's the whole integration point.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol

from dotenv import dotenv_values

MATCHING_PIPELINE_ENV = "/home/esau/ihc/matching_pipeline/.env"
SKILLOPT_ENV = "/home/esau/SkillOpt/.env.example"


def _env(*paths: str) -> dict:
    merged: dict = {}
    for path in paths:
        merged.update(dotenv_values(path))
    return merged


class ChatProvider(Protocol):
    name: str

    def chat(self, system_prompt: str, history: list[dict]) -> str:
        """history: list of {"role": "user"|"assistant", "content": str}."""
        ...


@dataclass
class DeepSeekProvider:
    name: str = "deepseek"

    def __post_init__(self):
        env = _env(SKILLOPT_ENV)
        from openai import OpenAI

        self._client = OpenAI(
            api_key=env["DEEPSEEK_CHAT_API_KEY"],
            base_url=env.get("DEEPSEEK_CHAT_URL", "https://api.deepseek.com/v1"),
        )
        self._model = env.get("DEEPSEEK_CHAT_MODEL", "deepseek-chat")

    def chat(self, system_prompt: str, history: list[dict]) -> str:
        messages = [{"role": "system", "content": system_prompt}, *history]
        resp = self._client.chat.completions.create(model=self._model, messages=messages)
        return resp.choices[0].message.content


@dataclass
class GeminiProvider:
    name: str = "gemini"
    model: str = "gemini-flash-latest"

    def __post_init__(self):
        env = _env(MATCHING_PIPELINE_ENV)
        from google import genai

        self._client = genai.Client(api_key=env["GEMINI_API_KEY"])

    def chat(self, system_prompt: str, history: list[dict]) -> str:
        from google.genai import types

        chat = self._client.chats.create(
            model=self.model,
            config=types.GenerateContentConfig(system_instruction=system_prompt),
        )
        last = ""
        for turn in history:
            if turn["role"] == "user":
                last = chat.send_message(turn["content"]).text
        return last


@dataclass
class ClaudeProvider:
    name: str = "claude"
    model: str = "claude-sonnet-4-5"

    def __post_init__(self):
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError(
                "ANTHROPIC_API_KEY no está configurada (no encontrada en el entorno "
                "ni en los .env conocidos). Este adaptador queda listo pero sin probar."
            )
        import anthropic

        self._client = anthropic.Anthropic(api_key=api_key)

    def chat(self, system_prompt: str, history: list[dict]) -> str:
        resp = self._client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=system_prompt,
            messages=history,
        )
        return "".join(block.text for block in resp.content if block.type == "text")


@dataclass
class OpenAIProvider:
    name: str = "openai"
    model: str = "gpt-4.1"

    def __post_init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY no está configurada. Este adaptador queda listo pero "
                "sin probar."
            )
        from openai import OpenAI

        self._client = OpenAI(api_key=api_key)

    def chat(self, system_prompt: str, history: list[dict]) -> str:
        messages = [{"role": "system", "content": system_prompt}, *history]
        resp = self._client.chat.completions.create(model=self.model, messages=messages)
        return resp.choices[0].message.content


PROVIDERS = {
    "deepseek": DeepSeekProvider,
    "gemini": GeminiProvider,
    "claude": ClaudeProvider,
    "openai": OpenAIProvider,
}


def get_provider(name: str) -> ChatProvider:
    if name not in PROVIDERS:
        raise ValueError(f"Proveedor desconocido: {name!r}. Opciones: {list(PROVIDERS)}")
    return PROVIDERS[name]()
