from typing import Optional

from fastapi import APIRouter

from app import schemas

router = APIRouter()


def get_text_pages_and_notes(name: str) -> schemas.Text:
    pages = [
        schemas.pecha.Page(
            id=str(i),
            page_no=str(i),
            content=f"{name} page {i} content",
            name=f"Page {i}",
            notes_page_id="1",
        )
        for i in range(1, 3)
    ]

    notes = [
        schemas.pecha.NotesPage(
            id="1", page_no="1", content="note 1 content", name="Page 100"
        ),
        schemas.pecha.NotesPage(
            id="2", page_no="2", content="note 2 content", name="Page 100"
        ),
    ]
    return pages, notes


@router.get("/{pecha_id}/texts/{text_id}", response_model=schemas.Text)
def get_text(pecha_id: str, text_id: str, page_no: Optional[int] = None):
    pages, notes = get_text_pages_and_notes(pecha_id)
    if page_no:
        return schemas.Text(id=text_id, pages=[pages[0]], notes=notes)
    return schemas.Text(id=text_id, pages=pages, notes=notes)


@router.post("/predurma/save")
def save_text(text: schemas.Text):
    return f"Text {text.id} saved!"


@router.post("/pedurma/preview", response_model=schemas.PedurmaPreviewPage)
def pedurma_page_preview(
    google_page: schemas.Page,
    google_page_note: schemas.NotesPage,
    namsel_page: schemas.Page,
    namsel_page_note: schemas.NotesPage,
):
    content = f"This Page preview google page {google_page.page_no}"
    return schemas.PedurmaPreviewPage(content=content)
