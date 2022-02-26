def format_response(data, status=200):
    context = {
        'status': status,
        'data': data
    }
    return context