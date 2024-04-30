r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.preview.marketplace.available_add_on.available_add_on_extension import (
    AvailableAddOnExtensionList,
)


class AvailableAddOnInstance(InstanceResource):
    """
    :ivar sid: The unique string that we created to identify the AvailableAddOn resource.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar description: A short description of the Add-on's functionality.
    :ivar pricing_type: How customers are charged for using this Add-on.
    :ivar configuration_schema: The JSON object with the configuration that must be provided when installing a given Add-on.
    :ivar url: The absolute URL of the resource.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.description: Optional[str] = payload.get("description")
        self.pricing_type: Optional[str] = payload.get("pricing_type")
        self.configuration_schema: Optional[Dict[str, object]] = payload.get(
            "configuration_schema"
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[AvailableAddOnContext] = None

    @property
    def _proxy(self) -> "AvailableAddOnContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AvailableAddOnContext for this AvailableAddOnInstance
        """
        if self._context is None:
            self._context = AvailableAddOnContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "AvailableAddOnInstance":
        """
        Fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AvailableAddOnInstance":
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """
        return await self._proxy.fetch_async()

    @property
    def extensions(self) -> AvailableAddOnExtensionList:
        """
        Access the extensions
        """
        return self._proxy.extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.AvailableAddOnInstance {}>".format(context)


class AvailableAddOnContext(InstanceContext):

    def __init__(self, version: Version, sid: str):
        """
        Initialize the AvailableAddOnContext

        :param version: Version that contains the resource
        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/AvailableAddOns/{sid}".format(**self._solution)

        self._extensions: Optional[AvailableAddOnExtensionList] = None

    def fetch(self) -> AvailableAddOnInstance:
        """
        Fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AvailableAddOnInstance:
        """
        Asynchronous coroutine to fetch the AvailableAddOnInstance


        :returns: The fetched AvailableAddOnInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AvailableAddOnInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    @property
    def extensions(self) -> AvailableAddOnExtensionList:
        """
        Access the extensions
        """
        if self._extensions is None:
            self._extensions = AvailableAddOnExtensionList(
                self._version,
                self._solution["sid"],
            )
        return self._extensions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Marketplace.AvailableAddOnContext {}>".format(context)


class AvailableAddOnPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> AvailableAddOnInstance:
        """
        Build an instance of AvailableAddOnInstance

        :param payload: Payload response from the API
        """
        return AvailableAddOnInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.AvailableAddOnPage>"


class AvailableAddOnList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the AvailableAddOnList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/AvailableAddOns"

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AvailableAddOnInstance]:
        """
        Streams AvailableAddOnInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AvailableAddOnInstance]:
        """
        Asynchronously streams AvailableAddOnInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AvailableAddOnInstance]:
        """
        Lists AvailableAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AvailableAddOnInstance]:
        """
        Asynchronously lists AvailableAddOnInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AvailableAddOnPage:
        """
        Retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AvailableAddOnPage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AvailableAddOnPage:
        """
        Asynchronously retrieve a single page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AvailableAddOnInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AvailableAddOnPage(self._version, response)

    def get_page(self, target_url: str) -> AvailableAddOnPage:
        """
        Retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AvailableAddOnPage(self._version, response)

    async def get_page_async(self, target_url: str) -> AvailableAddOnPage:
        """
        Asynchronously retrieve a specific page of AvailableAddOnInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AvailableAddOnInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AvailableAddOnPage(self._version, response)

    def get(self, sid: str) -> AvailableAddOnContext:
        """
        Constructs a AvailableAddOnContext

        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __call__(self, sid: str) -> AvailableAddOnContext:
        """
        Constructs a AvailableAddOnContext

        :param sid: The SID of the AvailableAddOn resource to fetch.
        """
        return AvailableAddOnContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Marketplace.AvailableAddOnList>"
