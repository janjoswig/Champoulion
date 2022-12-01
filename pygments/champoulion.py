"""Champoulion theme
"""

from pygments.style import Style
from pygments.token import (
    Keyword, Name, Comment, String, Error,
    Literal, Number, Operator, Other,
    Punctuation, Text, Generic,
    Whitespace
)

hex_white = "#ffffff"
hex_black = "#020122"
hex_grey = "#44475a"
hex_error_red = "#DB0B0B"  # "#E84141"

hex_light_red = "#F49090"
hex_red = "#E84848"

hex_dark_blue = "#531CB3"
hex_blue = "#1A8FE3"

hex_yellow = "#FFB627"  # "#E0B329"
hex_dark_yellow = "#C7662E"
hex_green = "#478570"
hex_purple = "#985D87"


class ChampoulionStyle(Style):

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Comment: f"{hex_light_red} italic",
        Comment.Hashbang: f"{hex_light_red} italic",
        Comment.Multiline: f"{hex_light_red} italic",
        Comment.Preproc: f"{hex_light_red} italic",
        Comment.Single: f"{hex_light_red} italic",
        Comment.Special: f"{hex_light_red} italic",

        Generic: hex_black,
        Generic.Deleted: hex_black,
        Generic.Emph: f"{hex_black} underline",
        Generic.Error: hex_error_red,
        Generic.Heading: f"{hex_black} bold",
        Generic.Inserted: f"{hex_black} bold",
        Generic.Output: hex_black,
        Generic.Prompt: hex_black,
        Generic.Strong: hex_black,
        Generic.Subheading: f"{hex_black} bold",
        Generic.Traceback: hex_black,

        Error: f"{hex_error_red} bold",

        Keyword: f"{hex_red}",
        Keyword.Constant: f"noinherit nobold {hex_dark_blue}",
        Keyword.Declaration: hex_red,
        Keyword.Namespace: hex_red,
        Keyword.Pseudo: hex_red,
        Keyword.Reserved: hex_red,
        Keyword.Type: hex_red,

        Literal: hex_red,
        Literal.Date: hex_red,

        Name: hex_black,
        Name.Attribute: hex_green,
        Name.Builtin: f"{hex_green} italic",
        Name.Builtin.Pseudo: f"{hex_red} italic",
        Name.Class: f"{hex_yellow} bold",
        Name.Constant: hex_red,
        Name.Decorator: hex_purple,
        Name.Entity: hex_error_red,
        Name.Exception: hex_error_red,
        Name.Function: f"{hex_green}",
        Name.Function.Magic: f"{hex_green} bold",
        Name.Label: hex_red,
        Name.Namespace: f"{hex_black} italic",
        Name.Other: hex_red,
        Name.Tag: hex_red,
        Name.Variable: hex_red,
        Name.Variable.Class: hex_red,
        Name.Variable.Global: hex_red,
        Name.Variable.Instance: hex_red,
        Name.Variable.Magic: hex_red,

        Number: hex_purple,
        Number.Bin: hex_purple,
        Number.Float: hex_purple,
        Number.Hex: hex_purple,
        Number.Integer: hex_purple,
        Number.Integer.Long: hex_purple,
        Number.Oct: hex_purple,

        Operator: hex_red,
        Operator.Word: f"{hex_red}",

        Other: hex_red,

        Punctuation: hex_black,
        Punctuation.Marker: hex_red,

        String: hex_blue,
        String.Affix: hex_red,
        String.Backtick: hex_blue,
        String.Char: hex_blue,
        String.Delimiter: hex_red,
        String.Doc: f"{hex_blue} italic",
        String.Double: hex_blue,
        String.Escape: hex_red,
        String.Heredoc: hex_red,
        String.Interpol: hex_red,
        String.Other: hex_red,
        String.Regex: hex_red,
        String.Single: hex_blue,
        String.Symbol: hex_red,

        Text: hex_red,

        Whitespace: f"{hex_black} underline"
    }
