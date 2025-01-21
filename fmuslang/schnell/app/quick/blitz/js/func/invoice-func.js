function createInvoice( invoiceNumber ) {
    return {
        invoiceNumber,
        items: []
    };
};

function clone( o ) {
    return JSON.parse( JSON.stringify( o ) );
};

function addItem( invoice, quantity, itemPrice, description ) {
    const newInvoice = clone( invoice ); 
    newInvoice.items.push( {
        quantity,
        itemPrice,
        description
    } );
    return newInvoice;
};

function calculateSum( invoice ) {
    const logReducer = (acc, item) => {
        console.log( 'acc, item:', acc, item );
        return acc + item.quantity * item.itemPrice;    
    }
    const reducer = (acc, item) =>
        acc + item.quantity * item.itemPrice;
    return invoice.items.reduce( logReducer, 0 );
};

const invoice1a = createInvoice( 1 );
const invoice2a = createInvoice( 2 );

const invoice1b = addItem( invoice1a, 2, 10, 'T-Shirt' );
const invoice1 = addItem( invoice1b, 3, 25, 'Bag' );

const invoice2b = addItem( invoice2a, 10, 1, 'Light bulb' );
const invoice2 = addItem( invoice2b, 2, 10, 'Pillow' );

console.log( 'Invoice1 sum:', calculateSum( invoice1 ) );
console.log( 'Invoice2 sum:', calculateSum( invoice2 ) );