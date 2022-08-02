import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';


@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.scss']
})
export class ChildComponent implements OnInit {
  @Input() employees:any;
  @Input() empDetail:any;
  clickCount1:number=0;
  @Output() clickCount: EventEmitter<number> = new EventEmitter<number>();
  constructor() {
   
   }

  ngOnInit(): void {
   
   
  }
  clickCountF()
  {
    this.clickCount1++;
    console.log(this.clickCount1)
    //this.clickCount = String(this.clickCount1);
    this.clickCount.emit(this.clickCount1)

  }

}
