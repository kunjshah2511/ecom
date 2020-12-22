import React, {useState,useEffect} from "react";

import {getProducts} from "./helper/coreapicalls";
import Base from "./Base"
import "../styles.css"
import Card from "./Card"

export default function Home() {

    const [products,setProducts]=useState([]);
    const [error,setError]=useState(false)

    const loadAllProducts =() => {
        getProducts()
        .then( data => {
            if(data.error){
                setError(data.error);
                console.log(error);
            }
            else{
                setProducts(data);
            }
        })
        .catch(err => console.log(error));
    };


    useEffect(()=>{
        loadAllProducts();
    },[]);

    return (
        <Base title="Superhero Merchandise" description="Welcome to T-shirt store">
        <div>
            <h1>Latest Collection</h1>
            <div className="row">
                {products.map( (product,index)=>{
                    return(
                        <div key={index} className="col-4 mb-4">
                            <Card product={product}/>
                        </div>
                    )
                })}
            </div>
        </div>
        </Base>
    );
}
