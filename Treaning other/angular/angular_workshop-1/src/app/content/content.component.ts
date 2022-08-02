import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-content',
  templateUrl: './content.component.html',
  styleUrls: ['./content.component.scss']
})
export class ContentComponent implements OnInit {
  imgurl:string = 'https://m.media-amazon.com/images/I/9188P4BpTsL._SL1500_.jpg'

  

  constructor() { 

  }

  ngOnInit(): void {
    
  }

}
