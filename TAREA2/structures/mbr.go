package structures

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"os"
	"time"
)

type MBR struct {
	Mbr_size           int32        // Tamaño del MBR en bytes
	Mbr_creation_date  float32      // Fecha y hora de creación del MBR
	Mbr_disk_signature int32        // Firma del disco
	Mbr_disk_fit       [1]byte      // Tipo de ajuste
	Mbr_partitions     [4]PARTITION // Particiones del MBR
}

// SerializeMBR serializa la estructura MBR y la escribe en un archivo en la ruta especificada.
func (mbr *MBR) SerializeMBR(path string) error {
	file, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE, 0644)
	if err != nil {
		return err
	}
	defer file.Close()

	err = binary.Write(file, binary.LittleEndian, mbr)
	if err != nil {
		return err
	}

	return nil
}

// DeserializeMBR deserializa la estructura MBR desde un archivo en la ruta especificada.
func (mbr *MBR) DeserializeMBR(path string) error {
	file, err := os.Open(path)
	if err != nil {
		return err
	}
	defer file.Close()

	mbrSize := binary.Size(mbr)
	if mbrSize <= 0 {
		return fmt.Errorf("tamaño de MBR inválido: %d", mbrSize)
	}

	buffer := make([]byte, mbrSize)
	_, err = file.Read(buffer)
	if err != nil {
		return err
	}

	reader := bytes.NewReader(buffer)
	err = binary.Read(reader, binary.LittleEndian, mbr)
	if err != nil {
		return err
	}

	return nil
}

// Print imprime la información del MBR en un formato legible.
func (mbr *MBR) Print() {
	creationTime := time.Unix(int64(mbr.Mbr_creation_date), 0)

	fmt.Printf("Tamaño del MBR: %d\n", mbr.Mbr_size)
	fmt.Printf("Fecha de Creación: %s\n", creationTime.Format(time.RFC3339))
	fmt.Printf("Firma del Disco: %d\n", mbr.Mbr_disk_signature)
}

// DeserializeMBR deserializa la estructura MBR desde un archivo en la ruta especificada y la retorna.
func DeserializeMBR(path string) (*MBR, error) {
	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	mbr := &MBR{}
	err = binary.Read(file, binary.LittleEndian, mbr)
	if err != nil {
		return nil, err
	}

	return mbr, nil
}
func CreateInitialMBR(path string) error {
	file, err := os.Create(path)
	if err != nil {
		return err
	}
	defer file.Close()

	// Set file size to 5MB
	if err := file.Truncate(5 * 1024 * 1024); err != nil {
		return err
	}

	mbr := MBR{
		Mbr_size:           5 * 1024 * 1024,
		Mbr_creation_date:  float32(time.Now().Unix()),
		Mbr_disk_signature: 123456, // Example signature
	}

	if err := binary.Write(file, binary.LittleEndian, &mbr); err != nil {
		return err
	}

	return nil
}
