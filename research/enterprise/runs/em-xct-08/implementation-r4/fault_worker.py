"""Test process only: terminate at an actual SQLite transaction boundary."""
from pathlib import Path
import json,os,sys
from sync_register import Register
db,command_file,result_file,point=sys.argv[1:]
request=json.loads(Path(command_file).read_text(encoding='utf-8'))
reg=Register(db)
def fault(at):
    if at==point:os._exit(73)
result=reg.execute(request['command'],request['actor'],request['now'],fault=fault if point!='none' else None)
Path(result_file).write_text(json.dumps(result),encoding='utf-8');reg.close()
