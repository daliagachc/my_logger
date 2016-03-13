# project name: pyranometer
# created by diego aliaga daliaga_at_chacaltaya.edu.bo
import inspect
import logging
import logging.config


def get_logger(
        level="ERROR",
        name='root',
        propagate=False
):
    # if name is None:
    #     frm = inspect.stack()[1]
    #     mod = inspect.getmodule(frm[0])
    #     logger = mod.__name__
    # else:
    #     logger = name
    logger = name
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,  # this fixes the problem

        'formatters': {
            'simple': {
                'format': "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            logger: {

                'handlers': ['console'],
                'level': level,
                'propagate': propagate
            }
        }
    })

    return logging.getLogger(logger)

