package analyzer

import (
	"TAREA2/commands"
	"errors"
	"fmt"
	"strings"
)

// Analyzer analiza el comando de entrada y llama a la función de análisis correspondiente.
// Soporta los comandos mkdisk, rep y execute.
func Analyzer(input string) (interface{}, error) {
	tokens := strings.Fields(input)
	if len(tokens) == 0 {
		return nil, errors.New("no se proporcionó ningún comando")
	}

	switch tokens[0] {
	case "mkdisk":
		return commands.ParserMkdisk(tokens[1:])
	case "rep":
		return commands.ParserRep(tokens[1:])
	case "execute":
		return commands.ParserExecute(tokens[1:])
	default:
		return nil, fmt.Errorf("comando desconocido: %s", tokens[0])
	}
}
