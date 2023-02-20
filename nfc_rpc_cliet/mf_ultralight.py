from base_command import BaseCommand

class MfUltralight(BaseCommand):
    def __init__(self):
        super().__init__(name='mfu')
        mfu_commands = {
            "info": self.info,
            "dump": self.dump,
            "read": self.read,
            "write": self.write,
        }
        self.commands.update(mfu_commands)

    def get_name(self):
        return self.name

    def info(self):
        print("MfUltralight info")

    def dump(self, page):
        print(f"MfUltralight dump page {page}")

    def read(self, page):
        print(f"MfUltralight read page {page}")

    def write(self, page, data):
        print(f"MfUltralight write {data} to page {page}")
