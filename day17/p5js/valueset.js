class ValueSet extends Array {

    constructor() {
        super();
    }

    has( val ) {
        return this.find( x => x.equals( val ) ) !== undefined;
    }

    add( val ) {
        if ( this.has( val ) ) {
            return;
        }
        this.push( val );
    }

    delete( val ) {
        const index = this.indexOf( val );
        if ( index >= 0 ) {
            this.splice( index, 1 );
        }
    }

}