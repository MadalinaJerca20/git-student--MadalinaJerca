import Student from './student'
import studentsListData from '../data/students-list'
import Subtitle from './subtitle'
import Button from './button'
import React, {useState} from 'react'


function List() {
    const [blackText, setBlackText] = useState(false);

    const toggleColor = () => {
        if (blackText === true) {
            setBlackText(false);
        } else {
            setBlackText(true);
        }
    }

    const [showStudentList, setStudentList] = useState(false);
    
    const setStudentListHandler = () => {
            showStudentList ? setStudentList(false) : setStudentList(true);
        }

    let proxy = [];

    if (showStudentList === true) {
        proxy = studentsListData
    } else {
        proxy = [];
    }
        

    return (
        <div>
                      
            <Button changeColor={toggleColor} buttonName="Toggle color"/>
            <Button changeColor={setStudentListHandler} buttonName="Show students"/>
            
            {
                proxy.map( (dateStudent) =>
                (
                    <Student
                        key={dateStudent.id}
                        data={dateStudent}
                        blackColor={blackText}
                        age='23'
                        toggleColor={toggleColor}
                    />
                )
                )
            }
        </div>
    )
}

export default List;