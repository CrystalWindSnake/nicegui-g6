from typing import Callable, Dict, List, Optional
from nicegui.element import Element
from nicegui import context as ng_context, Client as ng_client


class G6(
    Element,
    component="g6.js",
):
    def __init__(
        self,
        data: Dict,
        options: Optional[Dict] = None,
    ) -> None:
        super().__init__()
        self._props["data"] = data
        self._props["graphOptions"] = options or {}
        self.style("width: 100%; min-height: 16rem;")

        self.__deferred_task = DeferredTask()

        self._event_listener_map: Dict[str, Callable[..., None]] = {}

        def on_graph_event(e):
            event_name = e.args["eventName"]
            data = e.args["data"]

            if event_name in self._event_listener_map:
                self._event_listener_map[event_name](data)

        self.on("graph-event", on_graph_event)

    def on_graph_event(
        self, event: str, callback: Callable[..., None], args: List[str] = []
    ):
        @self.__deferred_task.register
        def _():
            self._event_listener_map[event] = callback
            self.run_method("onEvent", event, args)


class DeferredTask:
    def __init__(self):
        self._tasks = []

        async def on_client_connect(
            client: ng_client,
        ):
            await client.connected()

            for task in self._tasks:
                task()

            client.connect_handlers.remove(on_client_connect)  # type: ignore

        ng_context.get_client().on_connect(on_client_connect)

    def register(self, task: Callable[..., None]):
        if ng_context.get_client().has_socket_connection:
            task()
        else:
            self._tasks.append(task)
