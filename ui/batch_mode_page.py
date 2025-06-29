import tkinter as tk
import tkinter.filedialog as filedialog

from ui.components.button import Button
from ui.components.flex_container import FlexContainer
from ui.components.label import Label
import modules.media as Media
import modules.checker as Checker


class BatchModePage(tk.Frame):
    def __init__(self, parent, on_message) -> None:
        super().__init__(parent)
        self.parent = parent

        self.rings = []
        self.messages = {}
        self.result = {}

        self.on_message = on_message

        self.container = FlexContainer(self)
        self.container.pack(padx = 8, pady = 8)

        self.title = Label(self.container, "Batch Process by selecting files")
        self.title.pack(anchor = "center",  pady = 8)

        self.upload = Button(self.container, text = "Upload File", command = self._handle_import)
        self.upload.pack(anchor = "center", pady = 8, padx = 8, fill = "none")


        Label(self.container, "Export to")
        Button(self.container, text = "Select destination path for exports", command = self._destination_dialog)

    def _on_update(self, message):
        self.on_message(message)
        pass
        
    def _handle_import(self):
        dir = filedialog.askopenfilenames()

        self.paths, self.rings = Media.import_rings(dir)
        self.message = {}

        for x, ring in enumerate(self.rings):

            self.result[self.paths[x]] = Checker.check_all_properties(ring)
            boolean = [el for el in self.result.values()]
            self.message[f"Ring {x}"]= {
                "result" : all(boolean),
                "counterexample": "Rings are loaded and checked" if all(boolean) else "Some properties not satisfied"
            }
            self._on_update(self.message)


    def _destination_dialog(self):
        dir = filedialog.asksaveasfilename(defaultextension=".csv", initialfile="export")

        try:
            Media.export_batch_results(self.result, dir)
            self.message['Results are exported'] = {
                    "result": True,
                    "counterexample": ""
            }
            self._on_update(self.message)

        except Exception as e:
            self.message['Cannot export error'] = {
                "result": False, "counterexample": "Error: " + str(e)
            }
            self._on_update(self.message)

