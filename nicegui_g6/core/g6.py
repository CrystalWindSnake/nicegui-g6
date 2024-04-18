from typing import Callable, Dict, List, Optional, Union
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
        self,
        event: str,
        callback: Callable[..., None],
        args: Union[List[str], str, None] = None,
    ):
        """
        Register a callback for a graph event.

        [G6 Event Reference](https://g6.antv.vision/en/api/event)

        Args:
            event (str): event name
            callback (Callable[..., None]): callback function
            args (Union[List[str], str, None], optional): event arguments. Defaults to None.

        Example:
            The parameter `args` can be a list of strings.

            ```python
            def on_node_click(data):
                print(data)

            g6().on_graph_event("node:click", on_node_click, ["item"])
            ```

            The parameter `args` can be a string, in which case it acts as a JavaScript function used to extract event data.
            ```python
            def on_graph_event(data):
                print(data)

            g6().on_graph_event("node:mouseenter", on_graph_event, r"e=>({data:e.item._cfg.id})")
            ```


        """

        @self.__deferred_task.register
        def _():
            self._event_listener_map[event] = callback
            self.run_method("onEvent", event, args or [])


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
