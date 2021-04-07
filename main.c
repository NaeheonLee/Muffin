#include<stdio.h>
#define _USE_MATH_DEFINES	//자연상수 e를 사용하기 위한 정의, math헤더
#include<math.h>

void random(long* pn, float* pu) {	//난수발생기 함수

	*pn = *pn * 843314861 + 453816693;

	if (*pn < 0) {
		*pn = *pn + 2147483647;
		*pn = *pn + 1;
	}
	*pu = *pn * 0.4656612 * M_E - 9;

}

void main() {
	long n;		//seed값
	int limit;		//전체 모래알의 개수
	int count = 0;	//전체 모래알 중 원 안의 모래알의 개수를 count하는 변수
	float pu, X, Y, result;	//난수의 값, 원주율의 값을 위한 실수형 변수 

	printf(" < Monte Calro 시뮬레이션을 통해 원주율 구하기 > \n\n");
	printf("SEED 값을 입력하세요 : ");
	scanf_s("%d", &n);
	printf("LIMIT 값을 입력하세요 : ");
	scanf_s("%d", &limit);

	for (int i = 0; i <= limit; i++) {
		random(&n, &pu);
		pu = pu * 0.000000001;	/*난수의 값이 소수점 앞 10자리 실수로
								생성되기 때문에 일정 값을 곱하여 소수점 뒤로 보낸다. */
		while (1) {
			if (pu >= 1) {		/*난수가 1 이상인 경우 랜덤 함수를
								한 번 더 실행하여 새로운 난수 값을 받는다. */
				random(&n, &pu);
				pu = pu * 0.000000001;
				continue;
			}
			else {		//난수가 1보다 작으면 반복문을 끝낸다.
				break;
			}
		}
		X = pu;		//X에 랜덤한 값을 대입한다.

		random(&n, &pu);
		pu = pu * 0.000000001;	//위와 동일

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
		Y = pu;		//Y에 랜덤한 값을 대입한다.

		if ((X * X) + (Y * Y) <= 1) {
			count++;
		}
	}
	printf("\nCOUNT : %d\n", count);
	result = (float)count / (float)limit * 4;	/*실수형 변수에 정수형 변수끼리의 계산결과를
												대입하는 것이기 때문에 일시적으로 형변환을 해준다.*/
	printf("RESULT : %f\n", result);
	
	printf("hello, world")
}
