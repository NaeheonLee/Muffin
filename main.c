#include<stdio.h>
#define _USE_MATH_DEFINES	//�ڿ���� e�� ����ϱ� ���� ����, math���
#include<math.h>

void random(long* pn, float* pu) {	//�����߻��� �Լ�

	*pn = *pn * 843314861 + 453816693;

	if (*pn < 0) {
		*pn = *pn + 2147483647;
		*pn = *pn + 1;
	}
	*pu = *pn * 0.4656612 * M_E - 9;

}

void main() {
	long n;		//seed��
	int limit;		//��ü �𷡾��� ����
	int count = 0;	//��ü �𷡾� �� �� ���� �𷡾��� ������ count�ϴ� ����
	float pu, X, Y, result;	//������ ��, �������� ���� ���� �Ǽ��� ���� 

	printf(" < Monte Calro �ùķ��̼��� ���� ������ ���ϱ� > \n\n");
	printf("SEED ���� �Է��ϼ��� : ");
	scanf_s("%d", &n);
	printf("LIMIT ���� �Է��ϼ��� : ");
	scanf_s("%d", &limit);

	for (int i = 0; i <= limit; i++) {
		random(&n, &pu);
		pu = pu * 0.000000001;	/*������ ���� �Ҽ��� �� 10�ڸ� �Ǽ���
								�����Ǳ� ������ ���� ���� ���Ͽ� �Ҽ��� �ڷ� ������. */
		while (1) {
			if (pu >= 1) {		/*������ 1 �̻��� ��� ���� �Լ���
								�� �� �� �����Ͽ� ���ο� ���� ���� �޴´�. */
				random(&n, &pu);
				pu = pu * 0.000000001;
				continue;
			}
			else {		//������ 1���� ������ �ݺ����� ������.
				break;
			}
		}
		X = pu;		//X�� ������ ���� �����Ѵ�.

		random(&n, &pu);
		pu = pu * 0.000000001;	//���� ����

		while (1) {
			if (pu >= 1) {
				random(&n, &pu);
				pu = pu * 0.000000001;
				continue;
			}
			else {
				break;
			}
		}
		Y = pu;		//Y�� ������ ���� �����Ѵ�.

		if ((X * X) + (Y * Y) <= 1) {
			count++;
		}
	}
	printf("\nCOUNT : %d\n", count);
	result = (float)count / (float)limit * 4;	/*�Ǽ��� ������ ������ ���������� �������
												�����ϴ� ���̱� ������ �Ͻ������� ����ȯ�� ���ش�.*/
	printf("RESULT : %f\n", result);

}