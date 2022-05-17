from enum import Enum


class EventCategory(Enum):
    PAGE_INTERACTION = "page interaction"
    FORM_INTERACTION = "form interaction"


class PageInteractionNamesEnum(Enum):
    PAGE_VIEW = "pageview"
    CTA_CLICK = "cta click"


class FormInteractionNamesEnum(Enum):
    SUBMIT = "submit"
    CANCEL = "cancel"
