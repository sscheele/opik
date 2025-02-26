# This file was auto-generated by Fern from our API Definition.

from ..core.client_wrapper import SyncClientWrapper
import typing
from ..core.request_options import RequestOptions
from ..types.workspace_metadata import WorkspaceMetadata
from ..core.pydantic_utilities import parse_obj_as
from ..errors.not_found_error import NotFoundError
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper


class WorkspacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_workspace_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceMetadata
            Workspace metadata

        Examples
        --------
        from Opik import OpikApi

        client = OpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )
        client.workspaces.get_workspace_metadata()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/private/workspaces/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkspaceMetadata,
                    parse_obj_as(
                        type_=WorkspaceMetadata,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWorkspacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_workspace_metadata(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WorkspaceMetadata:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceMetadata
            Workspace metadata

        Examples
        --------
        import asyncio

        from Opik import AsyncOpikApi

        client = AsyncOpikApi(
            api_key="YOUR_API_KEY",
            workspace_name="YOUR_WORKSPACE_NAME",
        )


        async def main() -> None:
            await client.workspaces.get_workspace_metadata()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/private/workspaces/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkspaceMetadata,
                    parse_obj_as(
                        type_=WorkspaceMetadata,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
