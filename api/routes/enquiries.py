# api/routes/enquiries.py
# POST /enquiries — accepts a prospective student enquiry. Requires a valid JWT.

from fastapi import APIRouter, Depends
from api.schemas import EnquiryIn, EnquiryOut
from api.auth import get_current_user
from datetime import datetime, timezone

router = APIRouter()


@router.post("/enquiries", response_model=EnquiryOut, status_code=201)
def create_enquiry(enquiry: EnquiryIn, current_user: str = Depends(get_current_user)):
    """
    Accept and acknowledge a new enquiry from a prospective student.

    Pydantic validates the request body before this function runs; a missing or
    malformed field returns 422 automatically. The JWT dependency returns 401 if
    the token is absent or invalid.
    """
    received_at = datetime.now(timezone.utc).isoformat()

    return {
        "name":         enquiry.name,
        "email":        enquiry.email,
        "message":      enquiry.message,
        "received_at":  received_at,
        "confirmation": f"Thanks {enquiry.name}, we've received your message and will be in touch shortly.",
    }
