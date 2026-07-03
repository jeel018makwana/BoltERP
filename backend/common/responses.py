from rest_framework.response import Response
from rest_framework import status

def success_response(
        data=None,
        message = "Success",
        status_code = status.HTTP_200_OK,
):
    """
    Standard Success Response
    """

    return Response(
        {
            "success":True,
            "message": message,
            "data":data,
        },
        status=status_code,
    );

def error_response(
        message = "Something went wrong.",
        error = None,
        status_code = status.HTTP_400_BAD_REQUEST,
):
    """
    Standard Error Response
    """

    return Response(
        {
            "success":False,
            "message":message,
            "errors":errors,
        },
        status = status_code,
    )