class Invoice {
    constructor( invoiceNumber ) {
        this.invoiceNumber = invoiceNumber;
        this.items = [];
    }
    addItem( quantity, itemPrice, description ) {
        this.items.push( { 
            quantity, 
            itemPrice, 
            description 
        } );
    }
    get sum() {
        let sum = 0;
        for( let i = 0; i < this.items.length; ++i ) {
            let item = this.items[i];
            sum += item.quantity * item.itemPrice;
        }
        return sum;
    }
}

const invoice1 = new Invoice( 1 );
const invoice2 = new Invoice( 2 );

invoice1.addItem( 2, 10, 'T-Shirt' );
invoice1.addItem( 3, 25, 'Bag' );

invoice2.addItem( 10, 1, 'Light bulb' );
invoice2.addItem( 2, 10, 'Pillow' );

console.log( 'Invoice1 sum:', invoice1.sum );
console.log( 'Invoice2.sum:', invoice2.sum );
