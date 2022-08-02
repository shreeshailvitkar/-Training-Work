import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {
  products = [{
    productId: 1001,
    productName: 'Television',
    price: 55000,
    imgUrl: 'https://m.media-amazon.com/images/I/9188P4BpTsL._SL1500_.jpg',
    quantityAvaibale: 10,
    isAvailable: true
  },
  {
    productId: 1002,
    productName: 'Radio',
    price: 5000,
    imgUrl: 'https://m.media-amazon.com/images/I/71rAgfjT1jL._SL1484_.jpg',
    quantityAvaibale: 50,
    isAvailable: true
  },
  {
    productId: 1003,
    productName: 'Mac book Pro',
    price: 250000,
    imgUrl: 'https://m.media-amazon.com/images/I/81jMsojO7vL._SL1500_.jpg',
    quantityAvaibale: 100,
    isAvailable: true
  },
  {
    productId: 1004,
    productName: 'Samsung galaxy s21',
    price: 50000,
    imgUrl: 'https://m.media-amazon.com/images/I/81o-H5PLmeL._SL1500_.jpg',
    quantityAvaibale: 100,
    isAvailable: false
  }]

  constructor() { }

  ngOnInit(): void {
  }

}
