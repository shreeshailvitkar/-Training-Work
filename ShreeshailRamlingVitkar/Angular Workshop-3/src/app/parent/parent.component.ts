import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.scss']
})
export class ParentComponent implements OnInit {
  employees = [{
    userId: 1001,
    username: 'arunm',
    password: 'Test@123',
    name: 'Arun K Mishra',
    userType: 'Admin',
    isActiveUser: true
  },
  {
    userId: 1002,
    username: 'swanandb',
    password: 'Swanand@123',
    name: 'Swanand Bhave',
    userType: 'customer',
    isActiveUser: true
  }]
  empDetail = ''
  constructor() {
    console.log("obj typpppee"+typeof(this.employees))
   }
 
  ngOnInit(): void {
  }

  getEmp(emp:any)
  {
    console.log(emp)
    this.empDetail = emp;
  }
  count:number=0;
  takeCount(count:number)
  {
    console.log(count)
    this.count=count;
    //return count;
  }


}
