from typing import Any, List

from pydantic import Field, validator, BaseSettings, PostgresDsn


def parse_comma_separated(value: Any) -> Any:
    if not isinstance(value, str):
        return value

    return [item.strip() for item in value.split(",") if item]


class DjangoSettings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool = Field(
        default=False,
        description="Отключено по дефолту",
    )
    ALLOWED_HOSTS: List[str] = Field(
        default_factory=list, description="(localhost,127.0.0.1)"
    )
    CSRF_TRUSTED_ORIGINS: List[str] = Field(
        default=list,
        description="Trusted origins for CSRF checks.",
    )

    STATIC_URL: str = "static/"
    MEDIA_URL: str = "media/"

    parse_comma_separated_values = validator(
        "ALLOWED_HOSTS", "CSRF_TRUSTED_ORIGINS", pre=True, allow_reuse=True
    )(
        parse_comma_separated,
    )


class EnvSettings(BaseSettings):
    DJ: DjangoSettings

    POSTGRES_DSN: PostgresDsn

    class Config:
        env_nested_delimiter = "__"
        case_sensitive = True
        validate_all = True
