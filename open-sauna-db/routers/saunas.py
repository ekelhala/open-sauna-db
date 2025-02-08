from fastapi import APIRouter

router = APIRouter()

# Get
@router.get("/")
def get_all_saunas():
    pass

@router.get("/{sauna_id}")
def get_sauna(sauna_id: int):
    pass

#Post
@router.post("/")
def create_sauna():
    pass
