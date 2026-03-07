# api/routes/enquiries.py
# POST /enquiries — accepts a prospective student enquiry and saves it to the database.
# Requires a valid JWT.

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.schemas import EnquiryIn, EnquiryOut
from api.auth import get_current_user
from api.database import get_db
from api.models import Enquiry

router = APIRouter()


@router.post("/enquiries", response_model=EnquiryOut, status_code=201)
def create_enquiry(
    enquiry: EnquiryIn,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    Save a new enquiry to the database and return the saved record.

    The JWT dependency returns 401 if the token is absent or invalid.
    Pydantic validates the request body before this function runs; a missing or
    malformed field returns 422 automatically.
    """
    # Build the ORM object — received_at is set automatically by the column default.
    record = Enquiry(
        name=enquiry.name,
        email=enquiry.email,
        message=enquiry.message,
    )

    db.add(record)      # stage the new row
    db.commit()         # write it to the database
    db.refresh(record)  # reload the row so record.id and record.received_at are populated

    # Attach the confirmation message before returning — this field is not stored in the DB.
    record.confirmation = f"Thanks {enquiry.name}, we've received your message and will be in touch shortly."

    return record
