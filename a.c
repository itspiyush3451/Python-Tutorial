/* C-Prog. to create a Binary Search Tree & count total
   no. of Nodes & Leaf Nodes.                           */
#include<stdio.h>
#include<math.h>
int a=0,b=0;
struct Btree
 {
   struct Btree *lchild;
   int data;
   struct Btree *rchild;
 };
typedef struct Btree NODE;
NODE *getnode()
 {
   NODE *temp;
   temp=(NODE*)malloc(sizeof(NODE));
   printf("\n\n Enter the data : ");
   scanf("%d",&temp->data);
   temp->lchild=NULL;
   temp->rchild=NULL;
   return(temp);
 }
NODE *create()
 {
   NODE *temp,*ptr,*root;
   char ch;
   root=NULL;
   do
	{
	  temp=getnode();
	  if(root==NULL)
		root=temp;
	  else
	 {
	  ptr=root;
	  while(ptr!=NULL)
	   {
		  if(ptr->data>temp->data)
		  {
			if(ptr->lchild==NULL)
			{
				  ptr->lchild=temp;
				  break;
			}
			else
			   ptr=ptr->lchild;
		 }
		 else
		 {
			 if(ptr->rchild==NULL)
			 {
				  ptr->rchild=temp;
				  break;
			 }
			 else
			   ptr=ptr->rchild;
		 }
	   }//while
	} //else
	  printf("\n Add More (Y/N)? : ");
      ch=getche();
    }while(ch=='Y' || ch=='y');
   return(root);
 }
void count(NODE *h)
  {
    if(h!=NULL)
     {
	a++;
	count(h->lchild);
	if(h->lchild==NULL && h->rchild==NULL)
	  b++;
	count(h->rchild);
     }
  }

main()
  {
    NODE *header;
    header=create();
    printf("\n");
    count(header);
    printf("\n The total no. of nodes are : %d",a);
    printf("\n\n The total no. of leaf nodes are : %d",b);
  }

