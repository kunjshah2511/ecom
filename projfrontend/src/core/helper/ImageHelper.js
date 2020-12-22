import React from 'react'

 const ImageHelper = ({product})=> {
     const imageurl=product ? product.image 
     : `https://miro.medium.com/max/2400/1*pUEZd8z__1p-7ICIO1NZFA.png`
    return (
        <div className="rounded border border-success p-2">
            <img src={imageurl}
            style={{ maxHeight:"100%",maxWidth:"100%" }}
            className="mb-3 rounded"
            alt=""
            />
            
        </div>
    )
}

export default ImageHelper