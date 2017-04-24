"""
A response received to a Swagger API operation.
"""
import logging

__all__ = ["Response"]


log = logging.getLogger(__name__)


class Response:
    """A response received to a Swagger API operation.

    :param raw_response: The raw response.
    :type raw_response: pyswagger.io.Response
    """

    def __init__(self, raw_response):
        self._raw_response = raw_response

    @property
    def status(self):
        """HTTP status code of the response.

        :rtype: int
        """
        return self._raw_response.status

    @property
    def body(self):
        """Parsed response body converted to objects via the codec in use."""
        return self._raw_response.data

    @property
    def raw(self):
        """Raw response body.

        :rtype: bytes
        """
        return self._raw_response.raw

    @property
    def headers(self):
        """HTTP headers received on the response.

        Example format is ``{'Content-Type': [xxx, xxx]}``

        :rtype: dict(str, list(str))
        """
        return self._raw_response.header
