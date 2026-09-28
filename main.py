import sys

from dataprocessor.__main__ import main
from dataprocessor.interfaces.menu import menu_principal

if __name__ == "__main__":
    # sem argumentos abre o menu; com argumentos (--formato etc.) roda a CLI
    if len(sys.argv) == 1:
        menu_principal()
    else:
        sys.exit(main())
