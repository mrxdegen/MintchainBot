from typing import Any

from pydantic import BaseModel, field_validator, validator, model_validator


class RankData(BaseModel):
    id: int
    address: str
    ens: Any
    amount: int
    role: str
    rank: int


class AssetData(BaseModel):
    id: int
    uid: int
    reward: Any
    type: str = "energy"
    openAt: Any
    createdAt: str | None = None


class OpenBoxData(BaseModel):
    energy: int
    type: str = "energy"


class ClaimData(BaseModel):
    code: int
    result: int
    msg: str


class InjectData(BaseModel):
    code: int
    result: bool
    msg: str


class UserInfo(BaseModel):
    id: int
    treeId: int
    address: str
    ens: Any
    energy: int
    tree: int
    inviteId: int
    type: str = "normal"
    stake_id: int
    nft_id: int
    nft_pass: int
    signin: int
    code: Any
    createdAt: str
    invitePercent: int


class ResponseData(BaseModel):
    code: int
    result: Any | None = None
    msg: str


class LoginWalletData(BaseModel):
    class User(BaseModel):
        id: int
        address: str
        status: str
        inviteId: None | int
        twitter: None | str
        discord: None | str

    access_token: str
    user: User



class EnergyListData(BaseModel):
    class Energy(BaseModel):
        uid: list[str]
        amount: int
        includes: list[int]
        type: str
        id: str = None
        freeze: bool = None

        @model_validator(mode="before")
        @classmethod
        def validate_id(cls, values):
            if values["type"] != "daily":
                includes = [str(i) for i in values["includes"]]
                uid_str = "_".join(includes)
                values["id"] = f"{values['amount']}_{uid_str}"
            else:
                values["id"] = f"{values['amount']}_"

            return values

    result: list[Energy]


class TaskListData(BaseModel):
    class Task(BaseModel):
        id: int
        name: str
        amount: int
        isFreeze: bool
        spec: str
        claimed: bool | None = None

    result: list[Task]


class TurntableData(BaseModel):
    energy: int
    count: int
    usedEnergy: int
