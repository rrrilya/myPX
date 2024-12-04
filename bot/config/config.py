from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int = 20087555
    API_HASH: str = '35f37295f42f7825b4cbe66b4e49a6f1'

    PLAY_INTRO: bool = False
    INITIAL_START_DELAY_SECONDS: list[int] = [10, 240]  # in seconds
    ITERATION_SLEEP_MINUTES: list[int] = [60, 120]  # in minutes
    ENABLE_SSL: bool = True

    USE_REF: bool = False
    REF_ID: str = ""  # It would be great if you didn't change it, but I'm not stopping you
    TOURNAMENT_TEMPLATE_ID: int = 1480112288

    SLEEP_AT_NIGHT: bool = True
    NIGHT_START_HOURS: list[int] = [18, 20]  # 24 hour format in your timezone
    NIGHT_END_HOURS: list[int] = [3, 5]  # 24 hour format in your timezone
    ADDITIONAL_NIGHT_SLEEP_MINUTES: list[int] = [2, 45]  # in minutes
    ROUND_START_TIME_DELTA_MINUTES: int = 43  # in minutes
    ROUND_END_TIME_DELTA_MINUTES: int = 11  # in minutes

    CLAIM_PX: bool = True
    UPGRADE_BOOSTS: bool = True
    PAINT_PIXELS: bool = True
    COMPLETE_TASKS: bool = True
    PARTICIPATE_IN_TOURNAMENT: bool = True
    COMPLETE_QUESTS: bool = True
    COMPLETE_DANGER_TASKS: bool = False
    WATCH_ADS: bool = True
    USE_ALL_CHARGES: bool = True
    RESELECT_TOURNAMENT_TEMPLATE: bool = True

settings = Settings()  # type: ignore
