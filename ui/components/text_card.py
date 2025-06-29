
import tkinter as tk


class TextCard(tk.Frame):
    def __init__(self, parent, **kwargs):
        """
        lines: list of strings to render as separate centered lines
        kwargs: optional styling (bg, borderwidth, relief, etc.)
        """
        super().__init__(parent, **kwargs)

        self.configure(
            width = 400,
            height=400,
            borderwidth=2,
            relief="groove",
            padx=10,
            pady=10,
            background=kwargs.get("background", "#f0f0f0")
        )

        self.pack_propagate(False)

        self._line_widgets = []
        self._line_frame = tk.Frame(self, bg = self['background'])
        self._line_frame.pack(fill = "both", expand = False)

    def render(self, values: dict):
        for widget in self._line_widgets:
            widget.destroy()

        self._line_widgets.clear()
        
        for key, value in values.items():

            label = tk.Label(
                self._line_frame,
                text = key,
                anchor="center",
                justify="left",
                bg=self["background"]
                
            )

            if 'message' in value:
                label['text'] = value['message']


            if 'result' in value:

                if value['result'] == True:
                    label['text'] = '✅ ' + key
                    label['fg'] = "green"

                else :
                    label['text'] = '❌ ' + key
                    label['fg'] = 'red'

            label.pack(anchor="center", pady=2, fill="x")
            self._line_widgets.append(label)

            if 'counterexample' in value:
                counterexample = tk.Label(
                    self._line_frame,
                    text = '\t' + (value['counterexample'] if value['counterexample'] else "no counterexample defined"),
                    anchor = "center",
                    justify = "left",
                    bg = self['background']
                )


                counterexample.pack(anchor="center", pady = 2)
                self._line_widgets.append(counterexample)

