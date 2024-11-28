from win11toast import toast
from pathlib import Path

def empty_func(args):
    pass

toast('Hello Python🐍',
	'An Icon is displayed',
	icon=str(Path('fc0.ico').resolve()),
	
	on_dismissed=empty_func
)

