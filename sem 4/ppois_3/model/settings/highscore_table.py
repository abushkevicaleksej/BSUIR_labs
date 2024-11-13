class Highscore_table:
    def __init__(self, table, buttons, config):
        self.hs_table = table
        self.buttons = buttons
        self.config = config

    def update(self, name, score):
        self.hs_table[name] = score
        if len(self.hs_table) > self.config.get('max_records', 5):
            sorted_scores = sorted(self.hs_table.items(), key=lambda item: item[1], reverse=True)
            self.hs_table = dict(sorted_scores[:self.config.get('max_records', 5)])

    def print(self, x, y):
        step_x = 300
        step_y = 30
        sorted_scores = sorted(self.hs_table.items(), key=lambda item: item[1], reverse=True)[:self.config.get('max_records', 5)]
        for name, score in sorted_scores:
            self.buttons.draw_text(name, 30, x, y)
            self.buttons.draw_text(str(score), 30, x + step_x, y)
            y += step_y