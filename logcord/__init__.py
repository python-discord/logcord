import hug


@hug.get()
def health():
    return {'status': 'ok'}
