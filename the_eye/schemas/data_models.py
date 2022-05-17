from pydantic import BaseModel, constr


class PageInteractionPageviewData(BaseModel):
    host: constr(max_length=40)
    path: constr(max_length=40)


class PageInteractionCtaClickData(BaseModel):
    host: constr(max_length=40)
    path: constr(max_length=40)
    element: constr(max_length=20)


class SubmitForm(BaseModel):
    first_name: constr(max_length=20)
    last_name: constr(max_length=30)


class FormInteractionSubmitData(BaseModel):
    host: constr(max_length=40)
    path: constr(max_length=40)
    form: SubmitForm


class FormInteractionCancelData(BaseModel):
    host: constr(max_length=40)
    path: constr(max_length=40)
    reason: constr(max_length=25)
