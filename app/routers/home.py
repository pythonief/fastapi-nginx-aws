from fastapi import APIRouter, Query

router = APIRouter()

@router.get('/')
def index():
    return {
        'message': f'This is a demo fastapi with nginx in aws'
    }

@router.get('/hello')
def hello(q: str = Query('World')):
    return {
        'message': f'Hello {q}'
    }
