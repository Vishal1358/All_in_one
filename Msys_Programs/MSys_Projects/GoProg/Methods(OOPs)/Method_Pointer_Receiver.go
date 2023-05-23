package main

import "fmt"

type car struct {
	brand string
	price int
}

//declaring a method for car type
//it changes the value it works on
func changeCar(c car, newBrand string, newPrice int) {
	c.price = newPrice
	c.brand = newBrand
}

func (c car) changeCar1(newBrand string, newPrice int) {
	c.price = newPrice
	c.brand = newBrand

	//the changes are not seen to the outside world (pass by value)
}

// declaring a method with a pointer receiver
func (c *car) changeCar2(newBrand string, newPrice int) {
	(*c).brand = newBrand
	(*c).price = newPrice
	// the changes are seen the outside world
}

// method declarations are not permitted on named types that are themselves pointer types
type distance *int

// ERROR ->  invalid receiver type *distance (distance is a pointer type)
// func (d *distance) f() {
//  fmt.Println("say something")
// }

func main() {

	myCar := car{brand: "Audi", price: 250000}
	changeCar(myCar, "Renult", 200000)
	fmt.Println(myCar)

	// calling the method with a value receiver
	myCar.changeCar1("TATA Nano", 150000)
	// no change due to the same pass by value mechanism  !!!
	fmt.Println(myCar)

	// calling the method with a pointer receiver. It changes the value!
	(&myCar).changeCar2("Tata MoTo", 500000)
	fmt.Println(myCar)

	var yurcar *car
	yurcar = &myCar
	fmt.Println(*yurcar)

	// calling the method on pointer type
	// valid ways to call the method:
	(*yurcar).changeCar2("BMW", 250000)
	fmt.Println(*yurcar)

	// in the above example both myCar and yourCar variables have been modified.
	fmt.Println(myCar)
}
