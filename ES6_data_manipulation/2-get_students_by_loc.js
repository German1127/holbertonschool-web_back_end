const getStudentsByLocation = (students, city) => {
    const studentsLocation = students.filter(
        function (student) {
        return student.location === city;
    },
    );

    return studentsLocation;
  };

    export default getStudentsByLocation;