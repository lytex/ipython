import klembord
from prompt_toolkit.clipboard import Clipboard
from prompt_toolkit.filters.app import vi_navigation_mode, vi_selection_mode
from prompt_toolkit.key_binding.bindings.vi import create_operator_decorator, create_text_object_decorator

klembord.init()

ip = get_ipython()

if getattr(ip, 'pt_app', None):

    bindings = ip.pt_app.key_bindings
    operator = create_operator_decorator(bindings)
    text_object = create_text_object_decorator(bindings)


    @bindings.add('p', filter=vi_navigation_mode)
    def _(event):
        buf = event.current_buffer
        cp = None
        while cp is None:
            cp = klembord.get_text()
        buf.insert_text(cp)

    @bindings.add("x", filter=vi_selection_mode)
    def _cut(event):
        """
        Cut selection.
        ('x' is not an operator.)
        """
        clipboard_data = event.current_buffer.cut_selection()
        klembord.set_text(clipboard_data.text)

    @bindings.add("y", "y", filter=vi_navigation_mode)
    def _yank_line_extraline(event):
        """
        Yank the whole line.
        """
        text = "\n".join(event.current_buffer.document.lines_from_current[: event.arg])+"\n"
        klembord.set_text(text)

    @bindings.add("Y", filter=vi_navigation_mode)
    def _yank_line(event):
        """
        Yank the whole line.
        """
        text = "\n".join(event.current_buffer.document.lines_from_current[: event.arg])
        klembord.set_text(text)

    @operator("y")
    def _yank(event, text_object):
        """
        Yank operator. (Copy text.)
        """
        _, clipboard_data = text_object.cut(event.current_buffer)
        klembord.set_text(clipboard_data.text)

