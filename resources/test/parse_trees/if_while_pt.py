if_while_expected_parse_tree = ('program', [
    ('declaration-list', [
        ('type-specifier', ['int']),
        'ID',
        ('declaration', [
            ('var-declaration', [
                ('rest-of-var-declaration', ['[', 'NUM', ']'])
            ])
        ]),
        ('declaration-list', [
            ('fun-declaration', [
                '(',
                ('params', [
                    ('void-starting-param-list', [
                        'void',
                        ('rest-of-void-starting-param-list', []),
                    ])
                ]),
                ')',
                ('compound-stmt', [
                    '{',
                    ('declaration-list', [
                        ('declaration-list-prime', [
                            ('type-specifier', ['int']),
                            'ID',
                            ('declaration', [
                                ('var-declaration', [
                                    ('rest-of-var-declaration', [';']),
                                ]),
                            ]),
                        ]),
                        ('declaration-list-prime', []),
                    ]),
                    ('statement-list', [
                        ('statement-list-prime', [
                            ('statement', [
                                ('expression-stmt', [
                                    ('expression', [
                                        'ID',
                                        ('id-expression', [
                                            ('var', []),
                                            '=',
                                            ('expression', []),
                                        ]),
                                    ]),
                                    ';',
                                ]),
                            ]),
                            ('statement-list-prime', [
                                ('statement', [2222222]),
                                ('statement-list-prime', [
                                    ('statement', [333333]),
                                    ('statement-list-prime', [
                                        ('statement', [44444]),
                                        ('statement-list-prime', [
                                            ('statement', [555555]),
                                            ('statement-list-prime', [
                                                ('statement', [6666666]),
                                                ('statement-list-prime', [

                                                ]),
                                            ]),
                                        ]),
                                    ]),
                                ]),
                            ]),
                        ]),
                    ]),
                    '}',
                    ]),
                ]),
                ('declaration-list', []),
            ]),
    ]),
    'EOF',
])
