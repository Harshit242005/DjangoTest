# myapp/middleware.py
import logging
import datetime

def request_logger_middleware(get_response):
    print('Logging...')
    def middleware(request):
        print(f'Request method is {request.method}')
        print('Logging the request to the log files with this middleware')
        # Log request details
        log_data = {
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'method': request.method,
            'path': request.path,
        }

        log_message = f"{log_data['timestamp']} - {log_data['method']} request to {log_data['path']}"
        # Print log message to a file
        with open('request_info.txt', 'a') as file:
            file.write(log_message + '\n')
        logging.info(log_message)

        # Continue processing the request
        response = get_response(request)
        return response

    return middleware
