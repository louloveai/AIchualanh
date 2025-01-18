class ErrorHandler:
    def __init__(self):
        self.error_logs = []

    def log_error(self, error_type, message, context=None):
        error = {
            'type': error_type,
            'message': message,
            'context': context or {}
        }
        self.error_logs.append(error)
        return error

    def handle_error(self, error_type, message, context=None):
        error = self.log_error(error_type, message, context)
        if error_type == 'critical':
            raise Exception(message)
        return error 
