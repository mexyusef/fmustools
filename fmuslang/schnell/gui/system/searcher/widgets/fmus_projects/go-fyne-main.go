package main

import (
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
)

func main() {
	myApp := app.New()
	myWindow := myApp.NewWindow("Hello")

	hello := widget.NewLabel("Hello, World!")
	content := container.NewVBox(hello)

	myWindow.SetContent(content)
	myWindow.ShowAndRun()
}
