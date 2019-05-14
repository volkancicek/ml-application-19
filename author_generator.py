class AuthorGenerator:

    '''Two or More Authors
    When two or more authors work together on a source, write them in the order in which they appear on the source, using this format:
    Last name, F. M., & Last name, F. M., Last name, F. M., Last name, F. M., & Last name, F. M.
    Kent, A. G., & Giles, R. M. Thorpe, A., Lukes, R., Bever, D. J, & He, Y.
    If there are 8 or more authors listed on a source, only include the first 6 authors, add three ellipses, and then add the last author’s name.
    Roberts, A., Johnson, M. C., Klein, J., Cheng, E. V., Sherman, A., Levin, K. K. , ...Lopez, G. S.'''
    def get_author_names_in_apa_format(self, authors):
        if len(authors) == 0:
            return "[[[AUTHORS]]]"
        elif len(authors) == 1:
            return "%s" % tuple(authors)
        elif len(authors) == 2:
            return "%s, & %s"
        elif len(authors) >= 8:
            format_string = "%s, " * 6
            format_string += "...%s"
            return format_string % tuple(authors[:6] + [authors[-1]])
        else:
            format_string = "%s, " * (len(authors) - 1)
            return format_string + "& %s"


    def get_author_with_lastname_commablank_abbreviated_firstname_dot(self, first, last):
        full_name = "{0}, {1}".format(last, self.get_abbreviated_name(first))
        return full_name.title()

    def get_author_with_firstname_blank_lastname(self, first, last):
        full_name = "{0} {1}".format(first, last)
        return full_name.title()

    def get_author_with_lastname_commablank_firstname(self, first, last):
        full_name = "{0}, {1}".format(last, first)
        return full_name.title()

    def get_abbreviated_name(self, name):
        name_list = name.split()
        if len(name_list) == 0:
            return "[[[NAMES]]]"
        else:
            format_string = ""
            for i in range(len(name_list)):
                if i == (len(name_list) - 1):
                    format_string += "{d[" + str(i) + "][0]}."
                else:
                    format_string += "{d[" + str(i) + "][0]}. "
            return format_string.format(d=name_list)
