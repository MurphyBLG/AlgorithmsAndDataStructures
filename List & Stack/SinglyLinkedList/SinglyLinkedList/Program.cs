using System;
using System.Collections;
using System.Collections.Generic;

namespace SinglyLinkedList
{
    public class Record
    {
        public int Course { get; set; }
        public string GroupCode { get; set; }
        public string StudentSurname { get; set; }
        public DateTime ReceiptDate { get; set; }
        public string RecordBookNumber { get; set; }
        public string DisciplineName { get; set; }
        public int Mark { get; set; }

        public override string ToString()
        {
            return String.Format("Course: {0}\n" +
                "Group code: {1}\n" +
                "Student surname: {2}\n" +
                "Receipt date: {3}\n" +
                "Record book number: {4}\n" +
                "Discipline name: {5}\n" +
                "Mark: {6}\n\n", Course, GroupCode, StudentSurname, ReceiptDate, RecordBookNumber, DisciplineName, Mark);
        }
    }

    class SinglyLinkedList : IEnumerable
    {
        public class SinglyLinkedListNode
        {
            public Record Data { get; set; }
            public SinglyLinkedListNode Next { get; set; }

            public SinglyLinkedListNode(Record data)
            {
                this.Data = data;
            }
        }

        public SinglyLinkedListNode Head { get; set; }
        public SinglyLinkedListNode Tail { get; set; }
        public int Count { get; set; }

        public SinglyLinkedList()
        {
            this.Head = null;
            this.Tail = null;
            this.Count = 0;
        }

        public void Add(Record data)
        {
            SinglyLinkedListNode node = new SinglyLinkedListNode(data);

            if (this.Head == null)
                this.Head = node;
            else
                this.Tail.Next = node;

            this.Tail = node;
            this.Count++;
        }

        public void Clear()
        {
            this.Count = 0;
            this.Head = null;
            this.Tail = null;
        }

        private SinglyLinkedListNode GetMiddle(SinglyLinkedListNode l, SinglyLinkedListNode r)
        {
            if (l == null)
                return l;

            SinglyLinkedListNode fastptr = l.Next;
            SinglyLinkedListNode slowptr = l;

            while (fastptr != r && fastptr != r.Next)
            {
                fastptr = fastptr.Next;
                if (fastptr != r && fastptr != r.Next)
                {
                    slowptr = slowptr.Next;
                    fastptr = fastptr.Next;
                }
            }

            return slowptr;
        }

        public void MergeSort(SinglyLinkedListNode left, SinglyLinkedListNode right, string param)
        {
            if (left != right)
            {
                var mid = GetMiddle(left, right);
                this.MergeSort(left, mid, param);
                this.MergeSort(mid.Next, right, param);

                switch (param.ToLower())
                {
                    case "course":
                        this.MergeByCourse(left, mid, right);
                        break;
                    case "record book number":
                        this.MergeByRecordBookNum(left, mid, right);
                        break;
                    case "receipt date":
                        this.MergeByReceiptDate(left, mid, right);
                        break;
                }
            }
        }

        private void MergeByCourse(SinglyLinkedListNode left, SinglyLinkedListNode mid, SinglyLinkedListNode right)
        {
            var mainListPtr = left;
            SinglyLinkedList firstList = new SinglyLinkedList();
            while (mainListPtr != mid.Next)
            {
                firstList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }
            SinglyLinkedList secondList = new SinglyLinkedList();
            while (mainListPtr != right.Next)
            {
                secondList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }

            SinglyLinkedListNode firstListPtr = firstList.Head, secondListPtr = secondList.Head;
            mainListPtr = left;
            while (firstListPtr != null && secondListPtr != null)
            {
                if (firstListPtr.Data.Course < secondListPtr.Data.Course)
                {
                    mainListPtr.Data = firstListPtr.Data;
                    firstListPtr = firstListPtr.Next;
                } 
                else
                {
                    mainListPtr.Data = secondListPtr.Data;
                    secondListPtr = secondListPtr.Next;
                }

                mainListPtr = mainListPtr.Next;
            }

            while (firstListPtr != null)
            {
                mainListPtr.Data = firstListPtr.Data;
                mainListPtr = mainListPtr.Next;
                firstListPtr = firstListPtr.Next;
            }

            while (secondListPtr != null)
            {
                mainListPtr.Data = secondListPtr.Data;
                mainListPtr = mainListPtr.Next;
                secondListPtr = secondListPtr.Next;
            }
        }

        private void MergeByRecordBookNum(SinglyLinkedListNode left, SinglyLinkedListNode mid, SinglyLinkedListNode right)
        {
            var mainListPtr = left;
            SinglyLinkedList firstList = new SinglyLinkedList();
            while (mainListPtr != mid.Next)
            {
                firstList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }
            SinglyLinkedList secondList = new SinglyLinkedList();
            while (mainListPtr != right.Next)
            {
                secondList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }

            SinglyLinkedListNode firstListPtr = firstList.Head, secondListPtr = secondList.Head;
            mainListPtr = left;
            while (firstListPtr != null && secondListPtr != null)
            {
                if (String.Compare(firstListPtr.Data.RecordBookNumber, secondListPtr.Data.RecordBookNumber) < 0)
                {
                    mainListPtr.Data = firstListPtr.Data;
                    firstListPtr = firstListPtr.Next;
                }
                else
                {
                    mainListPtr.Data = secondListPtr.Data;
                    secondListPtr = secondListPtr.Next;
                }

                mainListPtr = mainListPtr.Next;
            }

            while (firstListPtr != null)
            {
                mainListPtr.Data = firstListPtr.Data;
                mainListPtr = mainListPtr.Next;
                firstListPtr = firstListPtr.Next;
            }

            while (secondListPtr != null)
            {
                mainListPtr.Data = secondListPtr.Data;
                mainListPtr = mainListPtr.Next;
                secondListPtr = secondListPtr.Next;
            }
        }

        private void MergeByReceiptDate(SinglyLinkedListNode left, SinglyLinkedListNode mid, SinglyLinkedListNode right)
        {
            var mainListPtr = left;
            SinglyLinkedList firstList = new SinglyLinkedList();
            while (mainListPtr != mid.Next)
            {
                firstList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }
            SinglyLinkedList secondList = new SinglyLinkedList();
            while (mainListPtr != right.Next)
            {
                secondList.Add(mainListPtr.Data);
                mainListPtr = mainListPtr.Next;
            }

            SinglyLinkedListNode firstListPtr = firstList.Head, secondListPtr = secondList.Head;
            mainListPtr = left;
            while (firstListPtr != null && secondListPtr != null)
            {
                if (firstListPtr.Data.ReceiptDate < secondListPtr.Data.ReceiptDate)
                {
                    mainListPtr.Data = firstListPtr.Data;
                    firstListPtr = firstListPtr.Next;
                }
                else
                {
                    mainListPtr.Data = secondListPtr.Data;
                    secondListPtr = secondListPtr.Next;
                }

                mainListPtr = mainListPtr.Next;
            }

            while (firstListPtr != null)
            {
                mainListPtr.Data = firstListPtr.Data;
                mainListPtr = mainListPtr.Next;
                firstListPtr = firstListPtr.Next;
            }

            while (secondListPtr != null)
            {
                mainListPtr.Data = secondListPtr.Data;
                mainListPtr = mainListPtr.Next;
                secondListPtr = secondListPtr.Next;
            }
        }

        public SinglyLinkedListNode Find(string param, string key)
        {
            switch (param.ToLower())
            {
                case "course":
                    return this.FindByCourse(int.Parse(key));
                case "record book number":
                    return this.FindByRecordBookNumber(key);
                case "receipt date":
                    return this.FindByReceiptDate(DateTime.Parse(key));
                default:
                    return null;
            }
        }

        private SinglyLinkedListNode FindByCourse(int course)
        {
            SinglyLinkedListNode current = Head;
            while (current != null)
            {
                if (current.Data.Course == course)
                    return current;
                current = current.Next;
            }

            return null;
        }

        private SinglyLinkedListNode FindByRecordBookNumber(string number)
        {
            SinglyLinkedListNode current = Head;
            while (current != null)
            {
                if (current.Data.RecordBookNumber == number)
                    return current;
                current = current.Next;
            }

            return null;
        }

        private SinglyLinkedListNode FindByReceiptDate(DateTime date)
        {
            SinglyLinkedListNode current = Head;
            while (current != null)
            {
                if (current.Data.ReceiptDate == date)
                    return current;
                current = current.Next;
            }

            return null;
        }

        public IEnumerator GetEnumerator()
        {
            SinglyLinkedListNode current = Head;
            while (current != null)
            {
                yield return current.Data;
                current = current.Next;
            }
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return ((IEnumerable)this).GetEnumerator();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            var records = new SinglyLinkedList();

            Console.WriteLine("Enter information about 3 students: ");
            for (int i = 0; i < 3; i++)
            {
                Console.Write("Course: ");
                int course = int.Parse(Console.ReadLine());
                Console.Write("Group code: ");
                string groupCode = Console.ReadLine();
                Console.Write("Student surname: ");
                string studentSurname = Console.ReadLine();
                Console.Write("Receipt date: ");
                DateTime receiptDate = DateTime.Parse(Console.ReadLine());
                Console.Write("Record book number: ");
                string recordBookNumber = Console.ReadLine();
                Console.Write("Discipline name: ");
                string disciplineName = Console.ReadLine();
                Console.Write("Mark: ");
                int mark = int.Parse(Console.ReadLine());
                Console.Clear();

                records.Add(new Record
                {
                    Course = course,
                    DisciplineName = disciplineName,
                    GroupCode = groupCode,
                    Mark = mark,
                    ReceiptDate = receiptDate,
                    RecordBookNumber = recordBookNumber,
                    StudentSurname = studentSurname
                });
            }

            Console.WriteLine("Initial list: ");
            foreach (var val in records)
                Console.Write(val.ToString());

            records.MergeSort(records.Head, records.Tail, "course");
            Console.WriteLine("Sorted by course: ");
            foreach (var val in records)
                Console.Write(val.ToString());

            records.MergeSort(records.Head, records.Tail, "record book number");
            Console.WriteLine("Sorted by record book number: ");
            foreach (var val in records)
                Console.Write(val.ToString());

            records.MergeSort(records.Head, records.Tail, "receipt date");
            Console.WriteLine("Sorted by receipt date: ");
            foreach (var val in records)
                Console.Write(val.ToString());
        }
    }
}
