from itertools import chain
import re

from coalib.bearlib.abstractions.SectionCreatable import SectionCreatable
from coalib.misc.Decorators import enforce_signature
from coalib.misc.Iterators import pairwise


class SpacingHelper(SectionCreatable):
    DEFAULT_TAB_WIDTH = 4

    def __init__(self, tab_width: int=DEFAULT_TAB_WIDTH):
        """
        Creates a helper object for spacing operations.

        :param tab_width: The number of spaces which visually equals a tab.
        """
        SectionCreatable.__init__(self)
        if not isinstance(tab_width, int):
            raise TypeError("The 'tab_width' parameter should be an integer.")

        self.tab_width = tab_width

    @enforce_signature
    def get_indentation(self, line: str):
        """
        Checks the lines indentation.

        :param line: A string to check for indentation.
        :return:     The indentation count in spaces.
        """
        count = 0
        for char in line:
            if char == ' ':
                count += 1
                continue

            if char == '\t':
                count += self.tab_width - (count % self.tab_width)
                continue

            break

        return count

    @enforce_signature
    def replace_tabs_with_spaces(self, line: str):
        """
        Replaces tabs in this line with the appropriate number of spaces.

        Example: " \t" will be converted to "    ", assuming the tab_width is
        set to 4.

        :param line: The string with tabs to replace.
        :return:     A string with no tabs.
        """
        for t_position, t_length in sorted(self.yield_tab_lengths(line),
                                           reverse=True):
            line = line[:t_position] + t_length * ' ' + line[t_position+1:]

        return line

    @enforce_signature
    def yield_tab_lengths(self, input: str):
        """
        Yields position and size of tabs in a input string.

        :param input: The string with tabs.
        """
        tabless_position = 0
        for index, char in enumerate(input):
            if char == '\t':
                space_count = (self.tab_width - tabless_position
                               % self.tab_width)
                yield index, space_count
                tabless_position += space_count
                continue

            tabless_position += 1

    @enforce_signature
    def replace_spaces_with_tabs(self, line: str):
        """
        Replaces spaces with tabs where possible. However in no case only one
        space will be replaced by a tab.

        Example: " \t   a_text   another" will be converted to
        "\t   a_text\tanother", assuming the tab_width is set to 4.

        :param line: The string with spaces to replace.
        :return:     The converted string.
        """
        currspaces = 0
        result = ""
        # Tracking the index of the string isnt enough because tabs are
        # spanning over multiple columns
        tabless_position = 0
        for char in line:
            if char == " ":
                currspaces += 1
                tabless_position += 1
            elif char == "\t":
                space_count = (self.tab_width - tabless_position
                               % self.tab_width)
                currspaces += space_count
                tabless_position += space_count
            else:
                result += currspaces*" " + char
                currspaces = 0
                tabless_position += 1

            # tabless_position is now incremented to point _after_ the current
            # char
            if tabless_position % self.tab_width == 0:
                if currspaces > 1:
                    result += "\t"
                else:
                    result += currspaces*" "

                currspaces = 0

        result += currspaces*" "

        return result

    @enforce_signature
    def highlight_whitespaces(self,
                              string: str,
                              show_spaces: bool=True,
                              space_replacement="•",
                              show_tabs: bool=True,
                              use_colors=False,
                              whitespace_color="cyan"):
        """
        Highlight whitespaces inside the given string using characters
        representing whitespaces.

        Spaces are replaced using ``space_replacement`` and is by default a
        bullet character. Tabs get arrow like visualization (like ``--->``).
        Depending on ``self.tab_width`` and the position of the tab, the arrow
        can be shorter or longer.

        >>> sh = SpacingHelper()
        >>> sh.highlight_whitespaces("\t\tstring where to highlight spaces.")
        '--->--->string•where•to•highlight•spaces.'

        Sometimes bullets are not the right choice, maybe dots are better:

        >>> sh = SpacingHelper()
        >>> sh.highlight_whitespaces("    white spaces!    ",
        >>>                          space_replacement='.')
        '....white.spaces!....'

        Often you print such highlighting to console. To display the spaces
        even better, some wants to use colors:

        >>> sh = SpacingHelper()
        >>> sh.highlight_whitespaces("\tsome spaces!", use_colors=True)
        [('cyan', '--->'), (None, 'some'), ('cyan', ' '), (None, 'spaces!')]

        :param string:            The string to highlight whitespaces in.
        :param show_spaces:       Whether to visualize spaces with
                                  ``space_replacement``.
        :param space_replacement: The character/string to replace spaces with
                                  when ``show_spaces`` is enabled.
        :param show_tabs:         Whether to use arrows (like ``--->``) to
                                  visualize tabs.
        :param use_colors:        Whether to annotate the string with colors
                                  that highlight the whitespaces.

                                  If ``False``, this functions returns a plain
                                  string. But if ``True``, portions of the
                                  given string are annotated with
                                  ``whitespace_color`` and this functions a
                                  list of tuples with the first element as the
                                  color annotation and the second one as the
                                  annotated string (e.g.
                                  ``[('cyan', '--->'), (None, 'text')]``).
                                  ``None`` is annotated for non-whitespace
                                  characters as a color.
        :param whitespace_color:  Arbitrary type to use as color-annotation
                                  for each substring. See ``use_colors``.
        :return:                  The highlighted string or a list of parts of
                                  strings annotated with ``whitespace_color``.
                                  See ``use_colors`` for more details.
        """
        match_patterns = []
        if show_spaces:
            match_patterns.append(" ")
        if show_tabs:
            match_patterns.append(r"\t")

        pattern_match_regex = "".join(match_patterns)
        complete_regex = ("([" + pattern_match_regex + "]+)([^" +
                          pattern_match_regex + "]+)")

        # We need to know the first match beforehand, that's why we keep the
        # iterator and reassemble the old sequence inside the for-loop later
        # using `chain()`.
        it = re.finditer(complete_regex, string)
        first_match = next(it)

        # The first non-whitespace-characters are not matched by the regex, so
        # let's prepend them beforehand.
        result = [(None, string[:first_match.start()])]

        # Process all matches, the first group matched are whitespaces that
        # shall be replaced and the second one is following
        # non-whitespace-text. Each match is then concatenated.
        for match in chain((first_match,), it):
            highlighted_match_string = match.group(1)

            if show_spaces:
                highlighted_match_string = highlighted_match_string.replace(
                    " ", space_replacement)

            if show_tabs:
                tab_it = self.yield_tab_lengths(highlighted_match_string)
                try:
                    # May raise a StopIteration when no tabs are inside the
                    # whitespace match. In this case we don't need to do
                    # anything.
                    first_tab = next(tab_it)

                    # This replaces all tabs with arrows like `--->`.
                    highlighted_match_string = (
                        highlighted_match_string[:first_tab[0]] + "".join(
                            "-" * (tab_length1 - 1) + ">" +
                            highlighted_match_string[pos1+1:pos2]
                            for (pos1, tab_length1), (pos2, tab_length2)
                            in pairwise(
                                chain((first_tab,),
                                      tab_it,
                                      ((len(highlighted_match_string), 0),)))))
                except StopIteration:
                    pass

            result.append((whitespace_color, highlighted_match_string))
            result.append((None, match.group(2)))

        if use_colors:
            return result
        else:
            return "".join(elem[1] for elem in result)
